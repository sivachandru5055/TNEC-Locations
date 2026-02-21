import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service';

@Injectable({
    providedIn: 'root'
})
export class AdminService {
    private http = inject(HttpClient);
    private authService = inject(AuthService);
    private apiUrl = 'http://192.168.60.1:8000';

    syncFees(): Observable<any> {
        const headers = new HttpHeaders({
            'Authorization': `Bearer ${this.authService.getToken()}`
        });
        return this.http.post(`${this.apiUrl}/admin/sync-fees`, {}, { headers });
    }
}
