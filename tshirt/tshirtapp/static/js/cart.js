var updateBtns = document.getElementsByClassName('update-cart')


for(var i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var womenId = this.dataset.women
        var action = this.dataset.action
        console.log('WomenId: ', womenId, 'Action: ', action)

        console.log('USER: ', user)
        if (user === 'AnonymousUser'){
            console.log('Not logged in')
        }
        else{
            updateUserOrder(womenId, action)
        }
    })

}


function updateUserOrder(womenId, action){
    console.log('User is logged in, sending data')

    var url = 'update_women'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({'womenId': womenId, 'action': action,})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data: ', data)
    })
}