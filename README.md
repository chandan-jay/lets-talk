lets_talk
=========

This App is built on Plivo API and Python<br/>


1. What this APP does?
   * It make call to two numbers and bridges then. So that they can talk to each other.


2. Which Plivo API is used?
   * The app implements API for outbound call and Dial Element in Answer_url XML. First call is fired by Outbound call API and the second call is fired by ```<Dial><Number>Dial Number</Number></Dial>``` XML.


3. How to use?

   * Sign Plivo and get a standard account.
   * Download the source from here.
   * Edit "routes.py" file to add your auth_ID and Auth_token. Also "answer_url". We recomend to build your own "answer_url" instead of using heroku answer_url link.
   * Upload to web server.


