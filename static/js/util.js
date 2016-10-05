var app;
app.ajax = function ajax(method,url,data,func){
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
