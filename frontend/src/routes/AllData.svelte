<script>
    //export let params = {}
    let data_list = []

    function get_all_data() {
        //let url = "/"+country+"/"+field+"/"
        //let params = {
        //    country: country,
        //    field: field 
        //}

        let method = 'GET' 
        let content_type = 'application/json'
        //let body = JSON.stringify(params)

        let _url = 'http://127.0.0.1:8888/api/data'
        //let _url = import.meta.env.VITE_SERVER_URL+url
        //if (method === 'GET') {
        //    _url += "?" + new URLSearchParams(params)
        //}

        let options = {
            method: method,
            headers: {
                "Content-Type": content_type
            }
        }

        fetch(_url, options)
            .then(response => {
                console.log('ok')

                response.json()
                    .then(json => {
                        if(response.status >= 200 && response.status < 300) {  // 200 ~ 299
                            for (let obj of json['data_list']){
                                data_list = [...data_list, JSON.stringify(obj, null, 2)]
                            }
                        }
                    })
                    .catch(error => {
                        alert(JSON.stringify(error))
                    })
        })
    }

</script>

<div class="container my-3">
    <div class="card my-3">
        <div class="card-body">
            <div class="my-3">
                <button class="btn btn-sm btn-outline-secondary" on:click={() => get_all_data()}>Get Data</button>
                <pre>{data_list}</pre>
            </div>
        </div>
    </div>
</div>

<style>
    textarea {
        width:100%;
    }
    input[type=submit] {
        margin-top:10px;
    }
</style>