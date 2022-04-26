# Endpoint-Scanner
Small script to check endpoints. The script is made for a specific purpose. After scanning endpoints in various javascript files, you often end up with a big list of endpoints that could look like this:

```
/admin/scheduler
/admin/securitygroup
/admin/system_properties
/admin/upload
```

The script is made to scan for any endpoints found, without authenticating. In the specific case I made it for, the endpoints were always redirected to `/login`. This script was made to find endpoints that did not require authentication. 

This script expects several parameters. These can be changed on line 8-10.

- BASE_URL : URL where endpoints will be appended to.
- HTML_THAT_CANNOT_INCLUDED : A string of text that appears on the authentication page, so the script knows this is not a valid alive endpoint.
- FILE_WITH_ENDPOINTS : A file in the same folder as the script that holds all the endpoints in the format that's above.


## Installation

This script depends on `requests` and the awesome `alive-progress`. 

```
pip3 install alive-progress
```

## Running

After setting the variables just run the script.




