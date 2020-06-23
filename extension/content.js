//let pathname = window.location.pathname;
//let url      = window.location.href;
let origin   = window.location.origin;

chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "clicked_browser_action" ) {
      console.log(origin);
    }
  }
);
