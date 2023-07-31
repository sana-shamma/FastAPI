<script>
  import { onMount } from "svelte";
  import Card from "../components/card.svelte";
  import Button from "../components/button.svelte";
  import MyWords from "../api/my_words";
  import PopupCard from "../components/popup_card.svelte";
  let myWords = new MyWords();
  $: words = [];

  onMount(() => {
    myWords.get_all_words().then((result) => {
      words = result;
    });
  });

  let showPopupCard = false;
  const toggleCard = () => {
    showPopupCard = !showPopupCard;
  };
</script>

<PopupCard bind:showPopupCard on:click={toggleCard} />

<header>
  <h1>Words Board</h1>
  <Button onClick={toggleCard} id="add" value="+ Add a Word" />
</header>

<div id="board">
  {#each words as word}
    <Card word={word.title} meaning={word.meaning} />
  {/each}
</div>

<style>
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: rgb(135, 181, 222);
    padding: 10px;
  }
  #board {
    background-color: rgb(233, 240, 240);
    padding: 10px;
    display: flex;
    gap: 10px;
    height: 100vh;
  }
  h1 {
    color: white;
  }
</style>
