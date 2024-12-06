<script>
  import Router from "svelte-spa-router"
  import AllData from "./routes/AllData.svelte"
  import CountryData from "./routes/CountryData.svelte"
  import FieldData from "./routes/FieldData.svelte"

  const routes = {
    "/": AllData,
    "/:country": CountryData,
    "/:country/:field": FieldData
  }

  //let message;

  //function g() {
  //  fetch("http://localhost:8000/api/data").then((response) => {
  //    response.json().then((json) => {
  //      message = json.msg;
  //      console.log(message)
  //    });
  //  });
  //}

  //g()
  
</script>

<!--h1>{message}</h1-->
<Router {routes}/>

