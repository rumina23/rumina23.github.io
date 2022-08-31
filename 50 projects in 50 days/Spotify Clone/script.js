console.log("Welcome to Spotify");

// Initialize the Variables
let songIndex = 0;
let audioElement = new Audio('songs/1.mp3');
let masterPlay = document.getElementById('masterPlay');
let myProgressBar = document.getElementById('myProgressBar');
let gif = document.getElementById('gif');
let masterSongName = document.getElementById('masterSongName');
let songItems = Array.from(document.getElementsByClassName('songItem'));

let songs = [
    {songName: "Ed Shreen - Shape of YOu", filePath: "songs/1.mp3", coverPath: "https://upload.wikimedia.org/wikipedia/en/b/b4/Shape_Of_You_%28Official_Single_Cover%29_by_Ed_Sheeran.png"},
    {songName: "Fake Love - BTS", filePath: "songs/2.mp3", coverPath: "6767.jpeg"},
    {songName: "My Head... - Ava Max", filePath: "songs/3.mp3", coverPath: "888.jpeg"},
    {songName: "Confetti - Little Mix", filePath: "songs/4.mp3", coverPath: "http://www.femalefirst.co.uk/image-library/partners/bang/square/500/l/little-mixs-confetti-0aa4a4efe027092cc705015fd1c0abb6c728259.jpg"},
    {songName: "Montero - Lis Nas", filePath: "songs/5.mp3", coverPath: "https://pyxis.nymag.com/v1/imgs/acb/00c/b7f75f4d87758910134354256ae0b66326-lil-nas-x-montero.rsquare.w330.jpg"},
    {songName: "Women - Doja Cat", filePath: "songs/6.mp3", coverPath: "https://i.pinimg.com/736x/1b/ce/bb/1bcebb1549e3c302861e236cef4b9ab1.jpg"},
    {songName: "The Motto - Invincible", filePath: "songs/7.mp3", coverPath: "https://pics.filmaffinity.com/Ti_sto_amp_Ava_Max_The_Motto_Music_Video-351626067-large.jpg"},
    {songName: "Bang Bang - Rita Ora", filePath: "songs/8.mp3", coverPath: "https://i1.sndcdn.com/artworks-jgzvKet7XtalCibw-8YKfDw-t500x500.jpg"},
    {songName: "Levitating - Dua Lipa", filePath: "songs/9.mp3", coverPath: "https://invest-in-albania.org/wp-content/uploads/dua.jpg"},
    {songName: "Permission to... - BTS", filePath: "songs/10.mp3", coverPath: "https://upload.wikimedia.org/wikipedia/en/0/04/BTS_-_Permission_to_Dance.png"},
]

songItems.forEach((element, i)=>{ 
    element.getElementsByTagName("img")[0].src = songs[i].coverPath; 
    element.getElementsByClassName("songName")[0].innerText = songs[i].songName; 
})
 

// Handle play/pause click
masterPlay.addEventListener('click', ()=>{
    if(audioElement.paused || audioElement.currentTime<=0){
        audioElement.play();
        masterPlay.classList.remove('fa-play-circle');
        masterPlay.classList.add('fa-pause-circle');
        gif.style.opacity = 1;
    }
    else{
        audioElement.pause();
        masterPlay.classList.remove('fa-pause-circle');
        masterPlay.classList.add('fa-play-circle');
        gif.style.opacity = 0;
    }
})
// Listen to Events
audioElement.addEventListener('timeupdate', ()=>{ 
    // Update Seekbar
    progress = parseInt((audioElement.currentTime/audioElement.duration)* 100); 
    myProgressBar.value = progress;
})

myProgressBar.addEventListener('change', ()=>{
    audioElement.currentTime = myProgressBar.value * audioElement.duration/100;
})

const makeAllPlays = ()=>{
    Array.from(document.getElementsByClassName('songItemPlay')).forEach((element)=>{
        element.classList.remove('fa-pause-circle');
        element.classList.add('fa-play-circle');
    })
}

Array.from(document.getElementsByClassName('songItemPlay')).forEach((element)=>{
    element.addEventListener('click', (e)=>{ 
        makeAllPlays();
        songIndex = parseInt(e.target.id);
        e.target.classList.remove('fa-play-circle');
        e.target.classList.add('fa-pause-circle');
        audioElement.src = `songs/${songIndex+1}.mp3`;
        masterSongName.innerText = songs[songIndex].songName;
        audioElement.currentTime = 0;
        audioElement.play();
        gif.style.opacity = 1;
        masterPlay.classList.remove('fa-play-circle');
        masterPlay.classList.add('fa-pause-circle');
    })
})

document.getElementById('next').addEventListener('click', ()=>{
    if(songIndex>=9){
        songIndex = 0
    }
    else{
        songIndex += 1;
    }
    audioElement.src = `songs/${songIndex+1}.mp3`;
    masterSongName.innerText = songs[songIndex].songName;
    audioElement.currentTime = 0;
    audioElement.play();
    masterPlay.classList.remove('fa-play-circle');
    masterPlay.classList.add('fa-pause-circle');

})

document.getElementById('previous').addEventListener('click', ()=>{
    if(songIndex<=0){
        songIndex = 0
    }
    else{
        songIndex -= 1;
    }
    audioElement.src = `songs/${songIndex+1}.mp3`;
    masterSongName.innerText = songs[songIndex].songName;
    audioElement.currentTime = 0;
    audioElement.play();
    masterPlay.classList.remove('fa-play-circle');
    masterPlay.classList.add('fa-pause-circle');
})