function Signup(URL){
    let username=document.getElementById("username").value;
    let email=document.getElementById("email").value;
    let password=document.getElementById("password").value;
    let re_password=document.getElementById("re_password").value;
    let which_condiction="signup";

    let data={
        username:username,
        email:email,
        password:password,
        re_password:re_password,
        which_condiction:which_condiction
        
    }


    if(username=="" && email=="" && password=="" && re_password ==""){
        alert("please enter all fields")
        }
else{
    if(password==re_password){
        SubmitData(data,URL,path='/')
    }
    else{
        alert("password dosent match")
    }
}
    }



function Login(URL){
    let username=document.getElementById("login_username").value;
    let password=document.getElementById("login_password").value;
    let which_condiction="login";

    let data={
        username:username,
        password:password,
        which_condiction:which_condiction
}
if(username=="" &&  password==""){
    alert("please enter all fields")
}
else{
    SubmitData(data,URL,path='/home')


}

}



function dataSent(){
    let event_month=document.getElementById("event_month").value;
    let fatality_count=document.getElementById("fatality_count").value;
    let injury_count=document.getElementById("injury_count").value;
    let population=document.getElementById("population").value;
    let longitude=document.getElementById("longitude").value;
    let latitude=document.getElementById("latitude").value;
    let landslide_category_complexity=document.getElementById("landslide_category_complex").value;
    let landslide_category_creep=document.getElementById("landslide_category_creep").value;
    let landslide_category_debris_flow =document.getElementById("landslide_category_debris_flow").value;
    let landslide_category_earth_fall =document.getElementById("landslide_category_earth_fall").value;
    let landslide_category_earth_flow =document.getElementById("landslide_category_earth_flow").value;
    let landslide_category_lahar =document.getElementById("landslide_category_lahar").value;
    let landslide_category_rock_fall = document.getElementById("landslide_category_rock_fall").value;
    let landslide_category_slide = document.getElementById("landslide_category_slide").value;
    let landslide_category_snow_avalanche = document.getElementById("landslide_category_snow_avalanche").value;
    let landslide_size_large = document.getElementById("landslide_size_large").value;
    let landslide_size_medium = document.getElementById("landslide_size_medium").value;
    let landslide_size_small= document.getElementById("landslide_size_small").value;
    let landslide_size_unknown = document.getElementById("landslide_size_unknown").value;

    let data={
        event_month:event_month,
        fatality_count:fatality_count,
        injury_count:injury_count,
        population:population,
        longitude:longitude,
        latitude:latitude,
        landslide_category_complexity:landslide_category_complexity,
        landslide_category_creep:landslide_category_creep,
        landslide_category_debris_flow:landslide_category_debris_flow,
        landslide_category_earth_fall:landslide_category_earth_fall,
        landslide_category_earth_flow:landslide_category_earth_flow,
        landslide_category_lahar:landslide_category_lahar,
        landslide_category_rock_fall:landslide_category_rock_fall,
        landslide_category_slide:landslide_category_slide,
        landslide_category_snow_avalanche:landslide_category_snow_avalanche,
        landslide_size_large:landslide_size_large,
        landslide_size_medium:landslide_size_medium,
        landslide_size_small:landslide_size_small,
        landslide_size_unknown:landslide_size_unknown
    }
    console.log(data)
    SubmitData(data,URL='/home',path='/home')


}
