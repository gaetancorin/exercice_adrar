import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-face-snap',
  templateUrl: './face-snap.component.html',
  styleUrls: ['./face-snap.component.scss']
})
export class FaceSnapComponent implements OnInit{
  title!: string;
  description!: string;
  createDate!: Date;
  snaps! : number;
  imageUrl! : string;
  buttonText! : string;

  ngOnInit(){
    this.title = "Mes vacances à la mer";
    this.description = "On a mangé des glaces";
    this.createDate = new Date();
    this.snaps = 6;
    this.imageUrl = "https://auxmerveilleux.com/city/440/croissant.jpg";
    this.buttonText = "J'apprécie !";
  }

  onSnap(){
      if(this.buttonText ==="J'apprécie !"){
        this.snaps++;
        this.buttonText = "Je n'apprécie plus";
      }
      else{
        this.snaps--;
        this.buttonText = "J'apprécie !";
      }
  }
}
