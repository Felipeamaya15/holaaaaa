import { Outlet } from 'react-router-dom';

import { VisualHeader } from './VisualHeader';
import { VisualBenefits } from './VisualBenefits';
import { VisualCTA } from './VisualCTA';
import { VisualFooter } from './VisualFooter';

export function VisualLayout() {
  return (
    <div className="template-visual min-h-screen bg-white text-[#111111] flex flex-col">
      <VisualHeader />

      <main className="flex-1">
        <Outlet />
      </main>

      <VisualBenefits />
      <VisualCTA />
      <VisualFooter />
    </div>
  );
}