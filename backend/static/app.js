document.getElementById("checkBtn").addEventListener("click", () => {
    const amount = document.getElementById("amount").value; // get value
    fetch(`/api/can-i-flex/?amount=${amount}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText =
                `Status: ${data.status}\nMessage: ${data.message}`;
        })
        .catch(err => {
            document.getElementById("result").innerText = "Error connecting to API.";
            console.error(err);
        });
});
