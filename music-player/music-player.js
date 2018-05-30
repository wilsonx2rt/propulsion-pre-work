function Player() {
  this.tracks = [];
  this.currentTrack = '';
  this.currentTrackNumber = null;
}

Player.prototype.add = function(track) {
  this.tracks.push(track);
}

Player.prototype.play = function() {
  this.currentTrack = this.tracks[0];
  this.currentTrackNumber = this.tracks.indexOf(this.currentTrack);
  this.currentTrack.printName();
}

Player.prototype.stop = function() {
  this.currentTrack = '';
  this.currentTrackNumber = null;
  console.log('Playbck stopped');
}

Player.prototype.next = function() {
  if(this.currentTrackNumber === this.tracks.length -1){
    this.currentTrack = this.tracks[0];
    this.currentTrackNumber = this.tracks.indexOf(this.currentTrack);
  } else {
    this.currentTrack = this.tracks[this.currentTrackNumber + 1];
    this.currentTrackNumber = this.tracks.indexOf(this.currentTrack);
  }
  this.currentTrack.printName();
}

Player.prototype.back = function() {
  if(this.currentTrackNumber === 0){
    this.currentTrack = this.tracks[this.tracks.length -1];
    this.currentTrackNumber = this.tracks.indexOf(this.currentTrack);
  } else {
    this.currentTrack = this.tracks[this.currentTrackNumber - 1];
    this.currentTrackNumber = this.tracks.indexOf(this.currentTrack);
  }
  this.currentTrack.printName();
}

Player.prototype.showPlayList = function() {
  console.log('Playlist =>');
  this.tracks.forEach(track => {
    console.log(`Song: ${track.title} By: ${track.artist} Album: ${track.album}`);
  });
}

Player.prototype.playSelection = function(trackName) {
  for (var i = 0; i < this.tracks.length; i++) {
    if(this.tracks[i].title == trackName) {
      this.currentTrack = this.tracks[i];
      this.currentTrackNumber = i;
      this.currentTrack.printName();
    }
  }
}
// skip tracks every 5 secs
// Player.prototype.playSkip = function(first) {
//   // strat from first track
//   if(first) { // takes true or false
//     this.play();
//     this.timerID = setInterval(() => this.next(), 3000);
//     setTimeout(()=> clearInterval(this.timerID), 7000)
//   } else {
//     this.timerID = setInterval(() => this.next(), 3000);
//     //this.timeOutID =
//   }
// }

Player.prototype.playSkip = function() {
  var that = this;
  that.currentTrackNumber = 0;
  that.interval = setInterval(function() {
    that.currentTrack = that.tracks[that.currentTrackNumber];
    that.currentTrack.printName();
    if (that.currentTrackNumber < that.tracks.length-1){
      that.currentTrackNumber++;
    }
    else clearInterval(that.interval);
  }, 2000);
}

// set time out for playback on last track
Player.prototype.playbackTimeOut = function() {
  setTimeout(() => clearInterval(this.timerID), 10000);
}

// ----------------------------- Track Class ----------------------------------

function Track(artist, title, album) {
  this.artist = artist;
  this.title = title;
  this.album = album;
}

Track.prototype.printName = function () {
    console.log(`Playing: ${this.title} by ${this.artist}`);
};

var driveTrack = new Track('Incubus', 'Drive', 'Make Yourself');
var laBambaTrack = new Track('Ritchie Valens', 'La Bamba', 'La Bamba');
var jamminTrack = new Track('Bob Marley', 'Jammin', 'Babylon by Bus');

// ----------------------------------------------------------------------------
var musicPlayer = new Player();

musicPlayer.add(driveTrack);
musicPlayer.add(laBambaTrack);
musicPlayer.add(jamminTrack);
musicPlayer.play();
console.log(musicPlayer.currentTrackNumber)
// musicPlayer.next();
// musicPlayer.next();
// musicPlayer.next();
// musicPlayer.playSelection('Jammin');
// musicPlayer.back();
// musicPlayer.showPlayList();

// musicPlayer.playSkip(true);
// musicPlayer.playbackTimeOut();
