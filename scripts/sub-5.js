let button = document.getElementById('submit-button')

button.addEventListener('click', ()=>{
    let answer = document.getElementById('input-for-question-5').value
    if(answer === "13.5" || answer === "13,5" || answer === "13.50" || answer === "13,50"){
        button.textContent="That's correct!"
        button.style.backgroundColor='green'
        button.style.color='white'
    }
    else if(answer == ""){
        console.log("Please fill out this field")
    }
    else{
        button.textContent="That's incorrect!"
        button.style.backgroundColor='red'
        button.style.color='white'
    }
})