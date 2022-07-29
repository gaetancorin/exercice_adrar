export class FaceSnap{
    title!: string;
    description!: string;
    createDate!: Date;
    snaps! : number;
    imageUrl! : string;
    location?: string;
}

// 2 eme Version, meme chose que 1ere version mais avec le raccourcis
// export class FaceSnap{
//     constructor(public title: string,
//                 public description: string,
//                 public createDate: Date,
//                 public snaps: number,
//                 public imageUrl: string,
//                 public location?: string
//                 ){
//     }
// }

// 1ere version sans le raccourcis mais sans le raccourcis
// export class FaceSnap{

//     title!: string;
//     description!: string;
//     createDate!: Date;
//     snaps! : number;
//     imageUrl! : string;
//     buttonText! : string;

//     constructor(title: string, description: string, createDate: Date, snaps: number, imageUrl: string,buttonText: string){
//         this.title = title;
//         this.description = description;
//         this.createDate = createDate;
//         this.snaps = snaps;
//         this.imageUrl = imageUrl;
//         this.buttonText = buttonText;
//     }

// }