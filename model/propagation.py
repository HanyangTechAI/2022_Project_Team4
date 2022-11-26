
from os import path
import numpy as np
import torch
import torch.nn.functional as F
from model.eval_network import PropagationNetwork
from inference_core import InferenceCore
import cv2
from detectron2.engine import DefaultPredictor
from detectron2.data import MetadataCatalog
from detectron2.config import get_cfg
from detectron2.utils.visualizer import ColorMode, Visualizer
from detectron2 import model_zoo

torch.autograd.set_grad_enabled(False)

CONST_e = 2.718282

class propagation:
    def __init__(self,video,index):
        if(index > 0 and index <= len(video)):
            self.indexFrame = video[index-1]
        else:
            print("index out of range. input should be in range 1~",len(video))
            quit()
        
        self.mask = None
        if(not(index == 1)):
            self.framesFront = video[:index]
            self.framesFront = torch.tensor(self.framesFront[::-1]).permute((0, 3, 1, 2))[None,:,:,:,:].cpu()
            self.framesFront = (self.framesFront -127.5)/127.5*CONST_e

        if(not(index == len(video))):
            self.frames = video[index:]
            self.frames = torch.tensor(self.frames).permute((0, 3, 1, 2))[None,:,:,:,:].cpu()
            self.frames = (self.frames -127.5)/127.5*CONST_e

        self.frameSize = []
        self.frameSize.append(torch.tensor([len(video[0])]))
        self.frameSize.append(torch.tensor([len(video[0][0])]))
        
        #model for Mask propagation
        prop_saved = torch.load('./Model/Mask-Propagation/saves/propagation_model.pth')
        top_k = None
        self.prop_model = PropagationNetwork(top_k=top_k, km=5.6).cuda().eval()
        self.prop_model.load_state_dict(prop_saved)


        #model for detectron image segmentation
        config_file = 'COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml'
        self.cfg = get_cfg()
        self.cfg.merge_from_file(model_zoo.get_config_file(config_file))
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.75 # Threshold
        self.cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(config_file)
        self.cfg.MODEL.DEVICE = "cuda" # cpu or cuda

        self.predictor = DefaultPredictor(self.cfg)
        self.output = self.predictor(self.indexFrame)

    def getMaskImage(self):

        v = Visualizer(self.indexFrame[:, :, ::-1],
               scale=0.8,
               metadata=MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]),
               instance_mode=ColorMode.IMAGE
               )

        return v.draw_instance_predictions(self.output["instances"].to("cpu")).get_image()[:, :, ::-1]

    def getSize(self):
        return (int(self.frameSize[1][0]),int(self.frameSize[0][0]))

    def getSelectedMask(self, XYCoordinates):
        masks = self.output["instances"].pred_masks


        for j in range(masks.shape[0]):
            if(masks[j][XYCoordinates[1]][XYCoordinates[0]] == True):
                selected_instances = self.output["instances"][j]
                break

        #여기서 self.mask를 지정합시다

        self.mask = selected_instances.pred_masks.unsqueeze(0).float().cuda()

        v = Visualizer(self.indexFrame[:, :, ::-1],
               scale=0.8,
               metadata=MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]),
               instance_mode=ColorMode.IMAGE
               )

        return v.draw_instance_predictions(selected_instances.to("cpu")).get_image()[:, :, ::-1]



    def process(self):
        if(self.mask == None):
            print("mask has not been selected")
            return []
        else:

            torch.cuda.synchronize()

            try:
                processor = InferenceCore(self.prop_model, self.frames, 1)
                processor.interact(self.mask, 0, self.frames.shape[1])
                # Do unpad -> upsample to original size 
                out_masks = torch.zeros((processor.t, 1, *self.frameSize), dtype=torch.uint8, device='cuda')
                for ti in range(processor.t):
                    prob = processor.prob[:,ti]

                    if processor.pad[2]+processor.pad[3] > 0:
                        prob = prob[:,:,processor.pad[2]:-processor.pad[3],:]
                    if processor.pad[0]+processor.pad[1] > 0:
                        prob = prob[:,:,:,processor.pad[0]:-processor.pad[1]]

                    prob = F.interpolate(prob, self.frameSize, mode='bilinear', align_corners=False)
                    out_masks[ti] = torch.argmax(prob, dim=0)
                out_masks = (out_masks.detach().cpu().numpy()[:,0]).astype(np.uint8)
            except:
                pass

            try:
                processorFront = InferenceCore(self.prop_model, self.framesFront, 1)
                processorFront.interact(self.mask, 0, self.framesFront.shape[1])
                out_masksFront = torch.zeros((processorFront.t, 1, *self.frameSize), dtype=torch.uint8, device='cuda')
                for ti in range(processorFront.t):
                    prob = processorFront.prob[:,ti]

                    if processorFront.pad[2]+processorFront.pad[3] > 0:
                        prob = prob[:,:,processorFront.pad[2]:-processorFront.pad[3],:]
                    if processorFront.pad[0]+processorFront.pad[1] > 0:
                        prob = prob[:,:,:,processorFront.pad[0]:-processorFront.pad[1]]

                    prob = F.interpolate(prob, self.frameSize, mode='bilinear', align_corners=False)
                    out_masksFront[ti] = torch.argmax(prob, dim=0)
                out_masksFront = (out_masksFront.detach().cpu().numpy()[:,0]).astype(np.uint8)
                out_masksFront = np.flip(out_masksFront, 0)
            except:
                pass

            torch.cuda.synchronize()
            
            try:
                return np.concatenate((np.flip(out_masksFront, 0), out_masks), axis=0)#선택한 index가 2~(마지막-1) 인 경우
            except:
                try:
                    return out_masksFront#선택한 index가 마지막인 경우
                except:
                    return out_masks#선택한 index가 1인 경우



