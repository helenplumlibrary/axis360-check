# Check Axis360 Links

## Instructions

This script accepts one argument, the path to an Excel file containing a `BTKey` column with a list of Baker & Taylor keys for Axis360 titles:

```
python axis360_check.py [filename.xlsx]
```

Each title key is appended to the `baseUrl` variable for the library's collection, and the URL is retrieved to see if the response contains the text "Error 404 Title Not Found." If so, that title key is printed on screen.

## License
This project is licensed under the terms of the [MIT license](LICENSE.txt).