import torch
import numpy as np

from .models.network_swinir import SwinIR

class SRModel:
    
    def __init__(self, upscaling=2):
        
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = SwinIR(upscale=upscaling, in_chans=3, img_size=64, window_size=8,
                            img_range=1., depths=[6, 6, 6, 6], embed_dim=60, num_heads=[6, 6, 6, 6],
                            mlp_ratio=2, upsampler='pixelshuffledirect', resi_connection='1conv').to(self.device)
        pretrained = torch.load(f"SwinIR/model_zoo/002_lightweightSR_DIV2K_s64w8_SwinIR-S_x{upscaling}.pth")
        self.model.load_state_dict(pretrained["params"] if "params" in pretrained.keys() else pretrained, strict=True)
        
    def inference(self, frames, batch_size=10):
        
        sr_output = []
        frames = torch.from_numpy(np.array(frames)/255).permute(0,3,1,2).float().cpu()
        
        self.model.eval()
        with torch.no_grad():
            for idx in range(0,len(frames),batch_size):
                frame_batch = frames[idx:idx+batch_size].to(self.device)
                sr_imgs = self.model(frame_batch).cpu()
                sr_output += [((img.permute(1,2,0).numpy())*255).astype(np.uint8) for img in sr_imgs]
                del frame_batch
                torch.cuda.empty_cache()
                
        return sr_output