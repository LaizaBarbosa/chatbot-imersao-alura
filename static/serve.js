function clearInput(){
        if(result){
                document.getElementById('text').value = ''
        }
}

function responseFormat(){
        const char = ["**", "*"]

        response = document.getElementById('modelResponse').value

        char.forEach(caracter => {
                if(char[0]){
                        response = response.split(caracter).join('')
                }else{
                        response = response.split(caracter).join(' ')
                }
        })

        return response
}