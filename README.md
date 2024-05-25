# ITNE352-Sec2-B3

Project title: client-server system for fetching news from NewsAPI.org<br>
Project description: this projects implements client and server python scripts that take user requests and retrieves news information as a response.<br>
Semester: 2023/2024 second term<br>
Group: B3<br>
Course code: ITNE352<br>
Section: 2<br>
Names: Abeer Mohammed Saleh Rozba 202102513 / Muna Abdullah Hussain 202103471<br>
<i>Requirements:</i><br><b>To set up the server:</b><br>
1- Clone this repository to your local machine then navigate to the server script.<br>
2- Install the requests library using pip to make HTTP requests.<br>
3- Replace the api_key value in the server script with your News API key.<br>
4- Run the server.<br>
<b>To set up the client:</b><br>
1- Navigate to the client script.<br>
2- Run the client.<br>
<i>Scripts description:</i><br>
<b>Server script:</b><br>
<i><b>Main functionality: </b></i> the server script creates a TCP server that listens to multiple client requests, then retrieves headlines and sources information from NewsAPI.org before sending them as a response to the client. </br>
<i><b>Packages: </b></i></br>
<i>socket: </i> creates a UDP or TCP socket (TCP in this project) and accepts client connection.<br>
<i>threading: </i> allows the server to accept multiple client connections simultaneously.<br>
<i>json: </i> is utilized to encode and decode json data.<br>
<i>requests: </i> enables to send HTTP requests to NewsAPI.org to fetch information.<br>
<i><b>Main functions: </b></i></br>
<i>handle_client(): </i> takes the client socket and address as parameters, accepts and announces the new connection before receiving, printing, and processing client request by calling handle_request() function.<br>
<i>handle_request(): </i> takes the request and client name as parameters, then checks and slices the request to find the sub option before calling the appropriate function to fetch the repsonse.
