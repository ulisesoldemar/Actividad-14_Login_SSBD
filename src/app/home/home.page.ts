import { Component, OnInit } from '@angular/core';
import { PeliculasService } from '../api/peliculas.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit{
  peliculas = []; // [
  //   {
  //     titulo: "Oldboy",
  //     anio: 2003,
  //     director: "Park Chan-wook",
  //     imagen: "https://cps-static.rovicorp.com/2/Open/TMDB4_2462/Program/4668894/_derived_jpg_q90_584x800_m0/Oldboy2003-Poster2x3.jpg"
      
  //   },
  //   {
  //     titulo: "Matrix",
  //     anio: 1999,
  //     director: "Hermanas Wachosky",
  //     imagen: "https://i.ebayimg.com/images/g/lwIAAOSwdPpbBbzT/s-l400.jpg"

  //   }
  // ];
  constructor(private peliculasService: PeliculasService) { }

  ngOnInit() {
    this.peliculasService.peliculas.subscribe(peliculas => {
      this.peliculas = peliculas;
    });
    this.peliculasService.getPeliculas();
  }

}
