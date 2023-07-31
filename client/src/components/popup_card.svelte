<script>
    export let showPopupCard;
    import InputField from "../components/inputField.svelte";
    import Button from "../components/button.svelte";
    import MyWords from "../api/my_words";
    let title = "";
    let meaning = "" ;
    let myWords = new MyWords()
    function add_word(){
        let newWord = { "title":title,"meaning":meaning}
        myWords.add_word(newWord);
        showPopupCard = false;
    }
</script>
  
  {#if showPopupCard}
    <div id="background" on:click|self >
      <div id="popup-message">
        <InputField bind:value={title} id="title" title="Title"/>
        <InputField bind:value={meaning} id="meaning" title="Meaning"/>
        <Button id="add" value="Add" onClick={add_word}/>
      </div>
    </div>
  {/if}
  
  <style>
    #background {
      width: 100vw;
      height: 100vh;
      position: fixed;
      z-index: 2000;
      background-color: rgba(0, 0, 0, 0.8);
    }
    #popup-message {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%,-50%);
      border-radius: 10px;
      width: 200px;
      height: 200px;
      padding: 30px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
      background-color: white;
      box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); 
    }
  </style>