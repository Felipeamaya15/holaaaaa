import { Outlet } from 'react-router-dom';
import { CatalogHeader } from './CatalogHeader';
import { CatalogFooter } from './CatalogFooter';

export function CatalogLayout() {
  return (
    <div className="template-catalog min-h-screen bg-[#050505] text-white flex flex-col">
      <CatalogHeader />
      <main className="flex-1">
        <Outlet />
      </main>
      <CatalogFooter />
    </div>
  );
}
