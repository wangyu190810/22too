var app = new Vue({
  el: '#app',
  data: {
    username: {
        "user":"asdfasdf"
    },
    user:"",
    pass:"",
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
    }
  }
})


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
