# ITNE352-Sec2-B3

<b>Project title: </b>client-server system for fetching news from NewsAPI.org<br>
<b>Project description: </b>this projects implements client and server python scripts that take user requests and retrieves news information as a response.<br>
<b>Semester: </b>2023/2024 second term<br>
<b>Group: </b>B3<br>
<b>Course code: </b>ITNE352<br>
<b>Section: </b>2<br>
<b>Names: </b>Abeer Mohammed Saleh Rozba 202102513 / Muna Abdullah Hussain 202103471<br>
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
<i>handle_request(): </i> takes the request and client name as parameters, then checks and slices the request to find the sub option before calling the appropriate function to fetch the repsonse.<br>
<b>Client script:</b><br>
<i><b>Main functionality: </b></i> the client establishes TCP connection with the server. It prints the main menu and sub menus according to the client's choice before sending his request to the server then receiving and printing the response.<br>
<i><b>Packages: </b></i></br>
<i>socket: </i> creates a TCP client socket and connects to the server.<br>
<i>json: </i> is utilized to encode and decode json data with the server.<br>
<i>time: </i> adds delays in client script.<br>
<i><b>Main functions: </b></i></br>
<i>print_main_menu(), print_headlines_menu(), print_sources_menu(): </i> display a menu and options for the user to choose from to filter the news information.
