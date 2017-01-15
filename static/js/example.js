var app = new Vue({
  el: '#app',
  data: {
    username: {
        "user":"asdfasdf"
    },
    user:"",
    pass:"",
    message:'cese',
    json_data:'',
    json_object:''
  },
  methods:{
    fetchDate:function(){
      var xhr = new XMLHttpRequest();
      var self = this;
      xhr.open("GET","/user/"+this.message.user,true);
      xhr.onload = function(){
        self.user = JSON.parse(xhr.responseText);
      }
      xhr.send(null);

    },
    get_user:function(url){
      var username = this.username.user
      userinfo(url,username);
    },
    login:function(url){
      login(url);
    },
    
    json_pares_method:function(){
      
      try {
        data =  JSON.parse(this.json_data)
        console.log(data)
        if (data instanceof Object){
            if (data instanceof Array ){
                var array_list = "<p>"
                for(i=0; i< data.length; i++){
                   var flag =  var_type(data[i]);
                   if(flag == 0){
                       if(is.Array(data[i])){
                           console.log(i+data[i])
                       }
                       var child_list = data[i]
                       for(j=0; j< child_list.length; j++){
                            array_list += child_list[j].toString() + "&nbsp&nbsp";
                       }
                   }else if (flag == 1){
                       array_list += data[i].toString() + "<p>";
                   }else if (flag == 2){
                        array_list += data[i] + "<p>"
                   }
                }
                console.log(array_list)
                this.json_object =array_list
          }
          else{

            this.json_object = data
          }
        }
      } catch (error) {
        console.log(error)
      }
      
    }
  }
})

var is ={
    types : ["Array", "Boolean", "Date", "Number", "Object", "RegExp", "String", "Window", "HTMLDocument"]
};
for(var i = 0, c; c = is.types[i ++ ]; ){
    is[c] = function(type){
        return function(obj){
           return Object.prototype.toString.call(obj) == "[object " + type + "]";
        }
    (c);
}
}

function var_type(data){
    // return 0 is Array
    // return 1 is Object
    if (data instanceof Object){
        if (data instanceof Array ){
            return 0
        }else{
            return 1
        }

    }
    return 2
}


function userinfo(url,username){
    var data = new FormData();
    data.append("username",username)
    function userinfo_callback(data){
        var user_data = JSON.parse(data);
        alert(user_data.username);
    }
    ajax("POST",url,data,userinfo_callback);


}



function login(url){

      var user = document.getElementById("user").innerHTML;
      var pass = document.getElementById("pass").innerHTML;
      var data = new FormData();
      // data.append("user","user");
      // data.append("pass","pass");
      data.append("user",user);
      data.append("pass",pass);

      function login_callback(data){
        var login_data = JSON.parse(data);
        alert(login_data.user);
      }
      ajax("POST",url,data,login_callback);

      //ajax("POST",url,data);
}

function upload(url){
    var oData = new FormData(document.forms.namedItem("fileinfo" ));
    function upload_callback(data){
      var upload_data = JSON.parse(data);
      alert(upload_data.msg);
    }
    ajax("POST",url,oData,upload_callback);



}
