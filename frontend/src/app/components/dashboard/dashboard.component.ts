import { Component, OnInit, inject, PLATFORM_ID, ChangeDetectorRef } from '@angular/core';
import { CommonModule, isPlatformBrowser } from '@angular/common';
import { RouterLink } from '@angular/router';
import { AdminService } from '../../services/admin.service';
import { AuthService } from '../../services/auth.service';

@Component({
    selector: 'app-dashboard',
    standalone: true,
    imports: [CommonModule, RouterLink],
    templateUrl: './dashboard.component.html',
    styles: []
})
export class DashboardComponent implements OnInit {
    private adminService = inject(AdminService);
    public authService = inject(AuthService);
    private platformId = inject(PLATFORM_ID);
    private cdr = inject(ChangeDetectorRef);
    syncMessage = '';

    // Target values
    private readonly targets = {
        total: 478,
        private: 407,
        govt: 71,
        anna: 407
    };

    // Initialize with targets so they show up immediately on server/pre-render
    displayTotal = this.targets.total;
    displayPrivate = this.targets.private;
    displayGovt = this.targets.govt;
    displayAnna = this.targets.anna;

    ngOnInit() {
        if (isPlatformBrowser(this.platformId)) {
            // In browser: start from 0 and animate
            this.displayTotal = 0;
            this.displayPrivate = 0;
            this.displayGovt = 0;
            this.displayAnna = 0;
            this.animateCounters();
        }
        // If not browser, we already initialized with targets above
    }

    animateCounters() {
        const duration = 2000; // 2 seconds
        const startTime = performance.now();

        const update = (currentTime: number) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);

            // Ease out cubic
            const easedProgress = 1 - Math.pow(1 - progress, 3);

            this.displayTotal = Math.floor(this.targets.total * easedProgress);
            this.displayPrivate = Math.floor(this.targets.private * easedProgress);
            this.displayGovt = Math.floor(this.targets.govt * easedProgress);
            this.displayAnna = Math.floor(this.targets.anna * easedProgress);

            // Force change detection
            this.cdr.detectChanges();

            if (progress < 1) {
                requestAnimationFrame(update);
            } else {
                // Ensure final targets are set
                this.displayTotal = this.targets.total;
                this.displayPrivate = this.targets.private;
                this.displayGovt = this.targets.govt;
                this.displayAnna = this.targets.anna;
            }
        };

        requestAnimationFrame(update);
    }

    syncFees() {
        this.syncMessage = 'Syncing...';
        this.adminService.syncFees().subscribe({
            next: (resp) => {
                this.syncMessage = resp.message;
            },
            error: (err) => {
                this.syncMessage = 'Error syncing fees: ' + err.message;
            }
        });
    }
}
