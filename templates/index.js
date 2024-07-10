const apiUrl = "https://api.api-ninjas.com/v1/weather?city=Singapore";

fetch(apiUrl, {
    headers: {
        "X-Api-Key": "XlPyiV+hD+kaN9l5kVpyQQ==zX6KpZBqPdOnrtCb"
    }
})
.then(response => {
    if(!response.ok) {
        throw new Error("Network response was not ok");
    } 
    return response.json();
})
.then(data => {
    document.getElementById("data").innerHTML = JSON.stringify(data);
})
.catch(error => {
    console.error("Error:", error);
});