# Server Information

## Endpoint explanation

1. `/upload`
- no parameters
- returns the video id as a string
2. `/time`
- no parameters
- receives the video id and time from the client
3. `/region`
- no parameters
- receives the video id
- generates the region by calling the function with the video id as the parameter
- returns the region via `send_file`
4. `/coordinates`
- no parameters
- receives the id and x, y coordinates
5. `/mask`
- no parameters
- if the user doesn't confirm, repeatedly send the masked image with the given x, y coordinates
- if the user confirms, process the video with the video id as the parameter
6. `/video`
- no parameters
- receives the video id
- generates the video by calling the function with the video id as the parameter
- returns the video via `send_file`
