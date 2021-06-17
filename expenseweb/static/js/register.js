const username = document.querySelector("username");

username.addEventListener('keyup',(e) => {
    console.log("777",777);
    const usernameval= e.target.value;

    if(usernameval.length > 0)
    {
        fetch("/authentication/username-val",
        {
            body: JSON.stringify({username: usernameval }),
            method:"POST",
        })
            .then((res) => res.json())
            .then((data) => { 
                console.log("data",data);
            });
    }
    


});