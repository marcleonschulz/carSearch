<script>
    import Nav from "./Nav.svelte";
    import Card from "./Card.svelte";

    let hsn, tsn;
    let result;

    async function getResult() {

        let response = await fetch(`http://162.55.208.18:8000/search-${hsn}-${tsn}`);
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
<div style="margin: 60%; margin-top: 5%; margin-left: 15%; margin-right: 15%;" className="grid-container">
    <form on:submit|preventDefault={submitHandler}>
        <p className="form-label">HSN</p>
        <input bind:value={hsn} className="form-input" type="text" id="input-example-1" placeholder="{tsn}">
        <p className="form-label">TSN</p>
        <input bind:value={tsn} className="form-input" type="text" id="input-example-2" placeholder="{tsn}">
        <button style="margin-top: 2%" className="btn">Suches</button>
    </form>

    {#if result === undefined}

        <p></p>

    {:else}

        {#await result}
            <p>Loading...</p>
        {:then value}
            {#if value.error}
                {value.error}
            {:else if value.handelsname && value.hersteller_name}
                <div style="margin-top: 5%;">
                    <Card css_color={""} header={`Suche für TSN: ${tsn} und TSN: ${hsn}`}
                          main={[`Hersteller :${value.hersteller_name}`,`Handelsname :${value.handel_name}`]}/>
                </div>
            {/if}
        {:catch error}
            <Card css_color={"text-error"} header={"Error"}
                  main={["Datenbank würd nicht gefunden", `Error Message ="${error.message}"`]}/>
        {/await}
    {/if}
</div>


<style>
</style>