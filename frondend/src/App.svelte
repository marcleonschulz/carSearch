<script>
    import Nav from "./Nav.svelte";
    import Card from "./Card.svelte";

    let hsn, tsn;
    let result;

    async function getResult() {

        let response = await fetch(`https://api.marc-schulz.tech/search-${hsn}-${tsn}`,{mode: "no-cors"});
        let text = await response.json();
        let data = text;
        return data;
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
                {value.error}
            {:else if value.handel_name && value.hersteller_name}
                <div style="margin-top: 5%;">
                    <Card css_color={""} header={`Suche für TSN: ${tsn} und TSN: ${hsn}`}
                          main={[`Hersteller :${value.hersteller_name}`,`Handelsname :${value.handel_name}`]}/>
                </div>
            {/if}
        {:catch error}
            <Card css_color={"text-error"} header={"Error"}
                  main={["Fehler beim erreichen der API!", `Error Message ="${error.message}"`]}/>
        {/await}
    {/if}
</div>


<style>
</style>