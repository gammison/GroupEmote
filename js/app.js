var apiKey = "45961152";
var sessionId = "2_MX40NTk2MTE1Mn5-MTUwNTU5NTI1MzE1Mn5ob0FKMzd3MGlERXVwNEVPOGtRNkVpUHF-fg";
var token = "T1==cGFydG5lcl9pZD00NTk2MTE1MiZzaWc9OTk3OWFmMzAwMDcxYTkyMWMwNDI4NDg3YWNjMDgzZTNjYzY0NjA5MDpzZXNzaW9uX2lkPTJfTVg0ME5UazJNVEUxTW41LU1UVXdOVFU1TlRJMU16RTFNbjVvYjBGS016ZDNNR2xFUlhWd05FVlBPR3RSTmtWcFVIRi1mZyZjcmVhdGVfdGltZT0xNTA1NTk1MjY4Jm5vbmNlPTAuMDk3NDU2NzgwMzczNDgwOTMmcm9sZT1wdWJsaXNoZXImZXhwaXJlX3RpbWU9MTUwNTU5ODg2OCZpbml0aWFsX2xheW91dF9jbGFzc19saXN0PQ==";

// (optional) add server code here
initializeSession();

// Handling all of our errors here by alerting them
function handleError(error) {
  if (error) {
    alert(error.message);
  }
}

function initializeSession() {
  var session = OT.initSession(apiKey, sessionId);

  // Subscribe to a newly created stream
  session.on('streamCreated', function(event) {
  session.subscribe(event.stream, 'subscriber', {
    insertMode: 'append',
    width: '100%',
    height: '100%'
  }, handleError);
});

  // Create a publisher
  var publisher = OT.initPublisher('publisher', {
    insertMode: 'append',
    width: '100%',
    height: '100%'
  }, handleError);

  // Connect to the session
  session.connect(token, function(error) {
    // If the connection is successful, publish to the session
    if (error) {
      handleError(error);
    } else {
      session.publish(publisher, handleError);
    }
  });
}