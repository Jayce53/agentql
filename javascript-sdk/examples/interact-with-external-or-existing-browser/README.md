# Example script: interact with external or existing browser

This is an example shows how to interact with external or existing browser by retrieving and interacting with web elements in AgentQL.

## Run the script

- [Install AgentQL SDK](https://docs.agentql.com/javascript-sdk/installation)
- Save this JS file locally as **interact-with-external-or-existing-browser.js**
- Close your Google Chrome application if it is open.
- If you're using **Mac**, open the terminal and run the following command:

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
```

- If you're using **Windows**, open the Command Prompt and run the command:

```bash
chrome.exe --remote-debugging-port=9222
```

**Make sure to replace `chrome.exe` with the path to your Chrome executable if it's not already in your system's PATH.**

- In the browser window that's opened, select the Google profile you would like to use for this session.

- In **interact-with-external-or-existing-browser.js**, replace variable `WEBSOCKET_URL`'s placeholder value with the actual WebSocket URL returned in terminal or command prompt. The URL should be in the format of `ws://127.0.0.1:9222/devtools/browser/387adf4c-243f-4051-a181-46798f4a46f4`.

- Run the following command from the project's folder:

```bash
node interact-with-external-or-existing-browser.js
```

- If you want to learn how to work with open pages, navigate to [Viator website](https://www.viator.com/Rome-tours/Walking-Tours/d511-g16-c56) within the browser, and use `fetch_data_from_open_website_page()` method in the script to fetch data from the page.

## Play with the query

Install the AgentQL Debugger Chrome extension to play with the AgentQL query. Learn more about the AgentQL query language