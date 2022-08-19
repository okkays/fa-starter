import { Component, OnInit } from '@angular/core';
import { CHARACTERS } from '../data/mock-characters';

@Component({
  selector: 'app-characters',
  templateUrl: './characters.component.html',
  styleUrls: ['./characters.component.css']
})
export class CharactersComponent implements OnInit {
  characterData = CHARACTERS;
  displayedColumns: string[] = ['name', 'race', 'class'];
  constructor() { }

  ngOnInit(): void {
  }


}
