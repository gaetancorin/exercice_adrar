import { Component, OnInit } from '@angular/core';
import { FaceSnap } from './models/face-snap.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  mySnap!: FaceSnap;
  myOtherSnap!: FaceSnap;
  myLastSnap!: FaceSnap;

  ngOnInit() {
    this.mySnap = new FaceSnap(
      "Mes vacances à la mer",
      "On a mangé des glaces",
      new Date(),
      6,
      "https://cdn.pixabay.com/photo/2017/01/20/00/30/maldives-1993704_960_720.jpg", "J'apprécie !");

    this.myOtherSnap = new FaceSnap(
      "Mes vacances à la montagne",
      "On a marché",
      new Date(),
      9,
      "https://cdn.pixabay.com/photo/2017/03/15/13/27/rough-horn-2146181_960_720.jpg", "J'apprécie !");

    this.myLastSnap = new FaceSnap(
      "Mon gouter",
      "On a mangé des croissants",
      new Date(),
      1,
      "https://auxmerveilleux.com/city/440/croissant.jpg", "J'apprécie !");
  }
  
}