import { Component, OnInit, AfterViewInit, inject, PLATFORM_ID } from '@angular/core';
import { CommonModule, isPlatformBrowser } from '@angular/common';
import { RouterLink, ActivatedRoute } from '@angular/router';
import { CollegeService, College } from '../../services/college.service';

// Color palette: one distinct color per zone (zone 1–9)
const ZONE_COLORS: Record<number, string> = {
    1: '#f59e0b', // amber  — Zone 1 (Thiruvallur)
    2: '#3b82f6', // blue   — Zone 2 (Kanchipuram W)
    3: '#10b981', // emerald — Zone 3 (South Chennai)
    4: '#8b5cf6', // violet — Zone 4 (Villupuram)
    5: '#ef4444', // red    — Zone 5
    6: '#06b6d4', // cyan   — Zone 6
    7: '#f97316', // orange — Zone 7
    8: '#ec4899', // pink   — Zone 8
    9: '#14b8a6', // teal   — Zone 9
    0: '#94a3b8', // slate  — unknown
};

const ZONE_NAMES: Record<number, string> = {
    1: 'Zone 1 – North',
    2: 'Zone 2 – West',
    3: 'Zone 3 – South Chennai',
    4: 'Zone 4 – South',
    5: 'Zone 5',
    6: 'Zone 6',
    7: 'Zone 7',
    8: 'Zone 8',
    9: 'Zone 9',
    0: 'Unclassified',
};

@Component({
    selector: 'app-map',
    standalone: true,
    imports: [CommonModule, RouterLink],
    templateUrl: './map.component.html',
    styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit, AfterViewInit {
    private map: any;
    private collegeService = inject(CollegeService);
    private platformId = inject(PLATFORM_ID);
    private route = inject(ActivatedRoute);

    public selectedCollege: College | null = null;
    private markers: Map<string, any> = new Map();
    private defaultCenter: [number, number] = [11.1271, 78.6569];
    private defaultZoom = 7;

    /** All zones that appear in current data */
    public availableZones: number[] = [];
    /** Zones that are currently visible on the map */
    public activeZones: Set<number> = new Set();

    public zoneColors = ZONE_COLORS;
    public zoneNames = ZONE_NAMES;

    ngOnInit(): void { }

    ngAfterViewInit(): void {
        if (isPlatformBrowser(this.platformId)) {
            // this.initMap(); // Disabled: Using Google My Maps Embed as requested
        }
    }

    private async initMap(): Promise<void> {
        try {
            const L = await import('leaflet');

            if (!document.getElementById('map')) {
                console.error('MapComponent: Map container element not found!');
                return;
            }

            this.map = L.map('map', {
                center: this.defaultCenter,
                zoom: this.defaultZoom
            });

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 18,
                minZoom: 6,
                attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            }).addTo(this.map);

            setTimeout(() => {
                if (this.map) this.map.invalidateSize();
            }, 500);

            this.loadColleges(L);
        } catch (error) {
            console.error('MapComponent: Error initializing map:', error);
        }
    }

    private loadColleges(L: any): void {
        this.collegeService.getColleges().subscribe({
            next: (colleges) => {
                const group = L.featureGroup();

                // Collect unique zones
                const zones = new Set<number>();
                colleges.forEach(c => zones.add(c.zone ?? 0));
                this.availableZones = Array.from(zones).sort((a, b) => a - b);
                this.activeZones = new Set(this.availableZones);

                colleges.forEach(college => {
                    const zone = college.zone ?? 0;
                    const color = ZONE_COLORS[zone] ?? ZONE_COLORS[0];

                    const marker = L.circleMarker([college.latitude, college.longitude], {
                        radius: 8,
                        fillColor: color,
                        color: '#fff',
                        weight: 2,
                        opacity: 1,
                        fillOpacity: 0.85
                    })
                        .addTo(this.map)
                        .bindPopup(`
                            <div style="font-family: 'Plus Jakarta Sans', sans-serif; min-width: 150px;">
                                <span style="font-size:0.75rem; padding:2px 8px; border-radius:99px; background:${color}22; color:${color}; font-weight:600;">${ZONE_NAMES[zone] ?? 'Zone ' + zone}</span><br>
                                <strong style="color: ${color};">${college.name}</strong><br>
                                <span style="color: #94a3b8; font-size: 0.8rem;">Code: ${college.code || 'N/A'}</span><br>
                                <span style="font-size: 0.85rem;">${college.location}</span>
                            </div>
                        `);

                    // Store marker with zone info for filtering
                    (marker as any)._zone = zone;
                    this.markers.set(college._id, marker);
                    marker.addTo(group);

                    marker.on('click', () => {
                        this.selectedCollege = college;
                    });
                });

                // Handle focus from URL query param
                this.route.queryParams.subscribe(params => {
                    const id = params['id'];
                    if (id && this.markers.has(id)) {
                        const college = colleges.find(c => c._id === id);
                        if (college) this.focusOnCollege(college);
                    } else if (colleges.length > 0 && !id) {
                        this.map.fitBounds(group.getBounds(), { padding: [50, 50] });
                    }
                });
            },
            error: (err) => {
                console.error('MapComponent: Error fetching colleges:', err);
            }
        });
    }

    /** Toggle a zone's visibility on the map */
    public toggleZone(zone: number): void {
        if (this.activeZones.has(zone)) {
            this.activeZones.delete(zone);
        } else {
            this.activeZones.add(zone);
        }
        // Rebuild a new Set reference so Angular detects the change
        this.activeZones = new Set(this.activeZones);
        this.applyZoneFilter();
    }

    public showAllZones(): void {
        this.activeZones = new Set(this.availableZones);
        this.applyZoneFilter();
    }

    public hideAllZones(): void {
        this.activeZones = new Set();
        this.applyZoneFilter();
    }

    private applyZoneFilter(): void {
        this.markers.forEach(marker => {
            const zone = (marker as any)._zone as number;
            if (this.activeZones.has(zone)) {
                if (!this.map.hasLayer(marker)) marker.addTo(this.map);
            } else {
                if (this.map.hasLayer(marker)) this.map.removeLayer(marker);
            }
        });
    }

    public isZoneActive(zone: number): boolean {
        return this.activeZones.has(zone);
    }

    public focusOnCollege(college: College): void {
        this.selectedCollege = college;
        const marker = this.markers.get(college._id);
        if (marker && this.map) {
            this.map.setView([college.latitude, college.longitude], 15, { animate: true });
            marker.openPopup();
        }
    }

    public clearView(): void {
        this.selectedCollege = null;
        if (this.map) {
            this.map.setView(this.defaultCenter, this.defaultZoom, { animate: true });
            this.map.closePopup();
        }
    }
}
