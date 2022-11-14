import {Button} from 'react-bootstrap';
import Link from 'next/Link';
import { useRouter } from 'next/router'

export default function Post() {
  const router = useRouter()
  const { juttuId, toinenId } = router.query;

  return  (
    <div>
        <h1>juttusivu</h1>
        <p>juttu id: {juttuId}</p>
        <p>toinen id: {toinenId}</p>
        <Button>
        <Link href="/joku/sivu">joku sivu</Link>
        </Button>
    </div>
  );
}