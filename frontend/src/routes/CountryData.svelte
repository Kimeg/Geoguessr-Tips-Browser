<script>
    //export let params = {}
    export let params = {}
    let country = params.country

    let _data = {}

    function get_country_data() {

        let method = 'GET' 
        let content_type = 'application/json'

        console.log(country)
        let _url = 'http://127.0.0.1:8888/api/data/'+country

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
                            _data = JSON.stringify(json, null, 2)
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
                <button class="btn btn-sm btn-outline-secondary" on:click={() => get_country_data()}>Get Data</button>
                <pre>{_data}</pre>
            </div>
        </div>
    </div>
</div>