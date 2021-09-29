<script>
    export let header;
    export let css_color;
    export let main = [];
</script>

<div class="card">
    <div class="card-header">
        <div class="{css_color} card-title h5">{header}</div>
    </div>
    <div class="card-body">
        {#each main as text}
            <p>{text}<p>
        {/each}
    </div>
</div>