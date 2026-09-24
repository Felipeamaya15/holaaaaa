import { useEffect } from 'react';
import { Outlet, useLocation } from 'react-router-dom';

import { MinimalSidebar } from './MinimalSidebar';
import { MinimalHeader } from './MinimalHeader';
import { MinimalFooter } from './MinimalFooter';

export function MinimalLayout() {
  const { pathname, search } = useLocation();

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [pathname, search]);

  return (
    <div className="template-minimal min-h-screen bg-[#f5f5f3]">

      <MinimalSidebar />

      <div className="md:pl-16 min-h-screen flex flex-col">

        <MinimalHeader />

        <main className="flex-1">
          <Outlet />
        </main>

        <MinimalFooter />

      </div>
    </div>
  );
}