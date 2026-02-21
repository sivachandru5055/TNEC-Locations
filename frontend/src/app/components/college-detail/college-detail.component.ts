import { Component, OnInit, inject, PLATFORM_ID, ChangeDetectorRef } from '@angular/core';
import { CommonModule, isPlatformBrowser } from '@angular/common';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';
import { CollegeService, College } from '../../services/college.service';

@Component({
    selector: 'app-college-detail',
    standalone: true,
    imports: [CommonModule, RouterLink],
    templateUrl: './college-detail.component.html',
    styles: []
})
export class CollegeDetailComponent implements OnInit {
    college: College | null = null;
    safeMapUrl: SafeResourceUrl | null = null;
    error: string | null = null;
    isLoading = true;
    private route = inject(ActivatedRoute);
    private collegeService = inject(CollegeService);
    private sanitizer = inject(DomSanitizer);
    private platformId = inject(PLATFORM_ID);
    private cdRef = inject(ChangeDetectorRef);

    ngOnInit(): void {
        // Only fetch data in the browser, not during SSR
        if (!isPlatformBrowser(this.platformId)) {
            return;
        }

        const id = this.route.snapshot.paramMap.get('id');
        console.log('College detail: loading ID =', id);
        if (id) {
            this.isLoading = true;
            this.collegeService.getCollegeDetails(id).subscribe({
                next: (data) => {
                    console.log('College detail: next() triggered with data:', data);
                    this.college = data;
                    if (this.college && (this.college.latitude || this.college.longitude)) {
                        console.log('College detail: setting safeMapUrl for', this.college.latitude, this.college.longitude);
                        const lat = this.college.latitude || 13.0827; // Fallback to Chennai
                        const lng = this.college.longitude || 80.2707;
                        const url = `https://www.openstreetmap.org/export/embed.html?bbox=${lng - 0.01},${lat - 0.01},${lng + 0.01},${lat + 0.01}&layer=mapnik&marker=${lat},${lng}`;
                        this.safeMapUrl = this.sanitizer.bypassSecurityTrustResourceUrl(url);
                    }

                    this.isLoading = false;
                    console.log('College detail: isLoading set to false. College present:', !!this.college);

                    // Force a change detection cycle in the next tick to ensure UI updates
                    setTimeout(() => {
                        this.cdRef.detectChanges();
                        console.log('College detail: manual change detection triggered');
                    }, 0);
                },
                error: (err) => {
                    console.error('College detail: error', err);
                    this.error = 'Failed to load college details. Please try again.';
                    this.isLoading = false;
                }
            });
        } else {
            this.error = 'Invalid college ID.';
            this.isLoading = false;
        }
    }

    printProfile() {
        window.print();
    }
}
