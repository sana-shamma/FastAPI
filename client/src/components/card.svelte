<script>
    import Button from "./button.svelte";
    import MyWords from "../api/my_words";
    export let word = "word";
    export let meaning = "meaning";
    let myWords = new MyWords() 

    function delete_word(){
         myWords.delete_word(word)
    }

    
    </script>
    
    <div id="main-container">
        <div id="title">{word}</div>
        <div id="content">Meaning: {meaning}</div>
        <div id="buttons-container">
            <Button onClick={delete_word} id="delete" value="Delete"/>
        </div>
    </div>
    
    <style>
    #main-container{
        border-radius: 10px;
        width: 200px;
        height: 200px;
        padding: 30px;
        display: flex;
        flex-direction: column;
        gap: 20px;
        background-color: white;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); 
    }
    #title{
        text-align: center;
        font-size: 20px;
    }
    #content{
        color: rgb(98, 101, 104);
    }
    #buttons-container{
        margin-left: auto;
        margin-right: auto;
        margin-top: auto;
    }
    </style>