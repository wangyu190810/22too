var vm  = new Vue({
    el: '#app',
    config:{
        url:"wwww.22too.com"
    },
    data :{
        title:"Vuejs",
        create_time: "2016-05-02",
        content:"学习Vuejs"
    },
    method:{
        index:function() {
            ajax("GET", config.url+"/api/index",null,index)      
        }
    }   
})


function index(data) {
    var index_dom = document.getElementById('index');
    var data = JSON.parse(data);
    for (var i=0; i< res.length; i++){
        index_dom = "<li>"+data.title+"</li>" + index_dom;
        index_dom = "<li>"+data.create_time+"</li>" + index_dom;
        index_dom = "<li>"+data.content+"</li>" + index_dom;
    }
}



function ajax(method,url,data,func){
            var xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function(){
                if(xhr.readyState == 4 && xhr.status == 200) {
                    var data = xhr.responseText;
                    func(data);
                    }
            }
            if (method === ( "get" && "GET")){
              xhr.open("GET",url,true);
              xhr.send();
            }
            else {
              xhr.open("POST",url,true);
              xhr.send(data);
            }
}
