const LAIKS = 1000;
async function suutiitZinju(){
    let vards = document.getElementById("vards").value;
    let zinja = document.getElementById("teksts").value;
    const atbilde = await fetch("/jschats/suutiit",{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"saturs": zinja, "vards": vards})
    }
    )

    
}

async function lasiitZinju() {
    const atbilde = await fetch("/jschats/lasiit");
    zinas = await atbilde.json()
    raadiitZinjas(zinas)
    await new Promise(resolve => setTimeout(resolve, LAIKS))
    await lasiitZinju()
}

function raadiitZinjas(saturs){
    let vieta = document.getElementById("chats");
    teksts = ""
    for(rinda of saturs){
        elementi = rinda.split("----")
        teksts += "<b>"+elementi[0]+"</b> - "+elementi[1]+ "<br>"
    }
    vieta.innerHTML = teksts
}


