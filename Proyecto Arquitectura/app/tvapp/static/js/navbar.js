const body = document.querySelector('body'),
      sidebar = body.querySelector('nav'),
      toggle = body.querySelector(".toggle"),
      searchBtn = body.querySelector(".search-box"),
      modeSwitch = body.querySelector(".toggle-switch"),
      modeText = body.querySelector(".mode-text");

      document.getElementById("icon_sol").style.display = "none";

toggle.addEventListener("click" , () =>{
    sidebar.classList.toggle("close");
})

searchBtn.addEventListener("click" , () =>{
    sidebar.classList.remove("close");
})

modeSwitch.addEventListener("click" , () =>{
    body.classList.toggle("dark");
    
    if(body.classList.contains("dark")){
        document.getElementById("icon_luna").style.display = "none";
        document.getElementById("icon_sol").style.display = "inline";
        
        modeText.innerText = "Light mode";
        
        
        

    }else{
        modeText.innerText = "Dark mode";
        document.getElementById("icon_luna").style.display = "inline";
        document.getElementById("icon_sol").style.display = "none";
        
    }
});
