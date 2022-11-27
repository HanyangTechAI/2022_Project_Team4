# Server Information

## Endpoint explanation

1. /upload
- no parameters
- returns the video id as string
2. /time
- no parameters
- receives the video id and time from the client
3. /region
- no parameters
- receives the video id
- generates the region by calling the function with the video id as the parameter
- returns the region via `send_file`
4. /coordinates
- no parameters
- receives the id and x, y coordinates
5. /mask
- no parameters
- repeatedly returns the masked image with x, y coordinates if the user doesn't confirm
- processes video if user confirms
6. /video
- no parameters
- receives the video id
- returns the processed video via `send_file`

