import { Component, OnInit } from '@angular/core';
import { FaceSnap } from './models/face-snap.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {

  faceSnaps!: FaceSnap[];

  ngOnInit() {
    this.faceSnaps = [
      {
        title: "Mes vacances à la mer",
        description: "On a mangé des glaces",
        createDate: new Date(),
        snaps: 6,
        imageUrl: "https://cdn.pixabay.com/photo/2017/01/20/00/30/maldives-1993704_960_720.jpg",
        location: "Perpignan",
      },
      {
        title: "Mes vacances à la montagne",
        description: "On a marché",
        createDate: new Date(),
        snaps: 90,
        imageUrl: "https://cdn.pixabay.com/photo/2017/03/15/13/27/rough-horn-2146181_960_720.jpg",
      },
      {
        title: "Mon gouter",
        description: "On a mangé des croissants",
        createDate: new Date(),
        snaps: 200,
        imageUrl: "https://auxmerveilleux.com/city/440/croissant.jpg",
        location: "Paris",
      },
    ]
  
}}