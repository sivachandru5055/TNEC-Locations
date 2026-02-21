import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service';

export interface College {
    _id: string;
    name: string;
    code?: string;
    website?: string;
    location: string;
    type: string;
    affiliated_to: string;
    fees_btech: number;
    fees_mtech: number;
    avg_package: number;
    latitude: number;
    longitude: number;
    location_url?: string;
    zone?: number;
}

@Injectable({
    providedIn: 'root'
})
export class CollegeService {
    private http = inject(HttpClient);
    private authService = inject(AuthService);
    private apiUrl = 'http://192.168.60.1:8000';

    getColleges(): Observable<College[]> {
        return this.http.get<College[]>(`${this.apiUrl}/colleges`);
    }

    getCollegeDetails(id: string): Observable<College> {
        return this.http.get<College>(`${this.apiUrl}/colleges/${id}`);
    }
}
