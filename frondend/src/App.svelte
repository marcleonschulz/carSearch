<script>
    import Nav from "./Nav.svelte";
    import Card from "./Card.svelte";
    let hsn = "";
    let tsn = "";
    let old_hsn, old_tsn = "";
    let result;
    async function getResult() {
        old_hsn = hsn;
        old_tsn = tsn;
        if(hsn != "" && tsn != ""){
            let response = await fetch(`https://api.marc-schulz.tech/search-${hsn}-${tsn}`);
            let text = await response.json();
            let data = text;
            return data;
        } else if (hsn != ""){
            let response = await fetch(`https://api.marc-schulz.tech/hsn-search-${hsn}`);
            let text = await response.json();
            let data = text;
            console.log(data)
            return data;
        } else {
            return {"error": "Sie haben nichts eingegeben!"}
        }
    }

    function submitHandler(e) {
        result = getResult();
        hsn = "";
        tsn = "";
    }
</script>
<Nav/>
<div style="margin: 60%; margin-top: 5%; margin-left: 15%; margin-right: 15%;" class="grid-container">
    <form on:submit|preventDefault={submitHandler}>
        <p class="form-label">HSN</p>
        <input bind:value={hsn} class="form-input" type="text" id="input-example-1" placeholder="{tsn}">
        <p class="form-label">TSN</p>
        <input bind:value={tsn} class="form-input" type="text" id="input-example-2" placeholder="{tsn}">
        <button style="margin-top: 2%" class="btn">Suches</button>
    </form>

    {#if result === undefined}

        <p></p>

    {:else}

        {#await result}
            <p>Loading...</p>
        {:then value}
            {#if value.error}
                {value.error} bei der Suche für HSN: "{old_hsn}" und TSN: "{old_tsn}"
            {:else if value.handel_name && value.hersteller_name}
                <div style="margin-top: 5%;">
                    {#if value.handel_name}
                    <Card css_color={""} header={`Suche für HSN: ${old_hsn} und TSN: ${old_tsn}`}
                          main={[`Hersteller :${value.hersteller_name}`,`Handelsname :${value.handel_name}`]}/>
                        {:else}
                        <Card css_color={""} header={`Suche für HSN: ${old_hsn}`}
                              main={[`Hersteller :${value.hersteller_name}`]}/>
                    {/if}
                </div>
            {/if}
        {:catch error}
            <Card css_color={"text-error"} header={"Error"}
                  main={["Fehler beim erreichen der API!", `Error Message ="${error.message}"`]}/>
        {/await}
    {/if}
</div>