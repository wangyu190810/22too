
ajax = function(method,url,data,func){
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

last = function(url){
    last_callback = function(data){
        var resp_json = JSON.parse(data);
        console.log(resp_json);
        document.getElementById("key").innerHTML = resp_json.key;
        document.getElementById("data").innerHTML = resp_json.data

    }
    var stmt;
    ajax("GET",url,stmt ,last_callback)
}

last("/api/api_lib_index")
