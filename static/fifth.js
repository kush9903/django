
const spinnerbox = document.getElementById('spinner-id')
const databox = document.getElementById('databox')
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  const wait=ms=>new Promise(resolve => setTimeout(resolve, ms));
var length2=0;


function ajaxCall(){
    
    $.ajax({
        type: 'GET',
        url: '/api/getdata',
        success: function(response){
            
            length2=JSON.stringify(response).length;
            if(length2 > 2){
                spinnerbox.classList.add('not-visible');
                for (x in JSON.stringify(response)) {
                    for(y in x){
                        console.log('response',  y);
                    }
                    console.log('response',  x);
                  }
                jsonif = JSON.stringify(response)
                console.log('response',  typeof response.column);
                $.ajax({
                    url: '/api/view',
                    success: function(response){},
                });
                console.log('response', response.json);
            }
            console.log('response', length2);
            
    },});
    };

var length1 = 2;
function repeator(){
    if(length2 == length1) {
        alert(length2);
        setTimeout(length, 300);
        console.log('resp');
        ajaxCall();
    }
    else {
        ajaxCall();
        }
};

var i;
for (i = 0; i < 10; i++) {
    console.log('resp',i);
    
}
ajaxCall();               



            
        



