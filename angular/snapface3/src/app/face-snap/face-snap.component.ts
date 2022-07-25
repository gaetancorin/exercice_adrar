import { Component, OnInit, Input } from '@angular/core';
import { FaceSnap } from '../models/face-snap.model';

@Component({
  selector: 'app-face-snap',
  templateUrl: './face-snap.component.html',
  styleUrls: ['./face-snap.component.scss']
})
export class FaceSnapComponent implements OnInit{
  @Input() faceSnap!: FaceSnap;

  buttonText! : string;

  ngOnInit(){
    this.buttonText = "J'apprécie !"
  }

  onSnap(){
      if(this.buttonText ==="J'apprécie !"){
        this.faceSnap.snaps++;
        this.buttonText = "Je n'apprécie plus";
      }
      else{
        this.faceSnap.snaps--;
        this.buttonText = "J'apprécie !";
      }
  }
}
